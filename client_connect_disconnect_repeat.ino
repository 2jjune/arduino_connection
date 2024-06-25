#include "WiFiS3.h"

// 네트워크 SSID와 비밀번호
char ssid[] = "MIPLAB311";        // 네트워크 SSID (이름)
char pass[] = "image123";         // 네트워크 비밀번호
int keyIndex = 0;                 // 네트워크 키 인덱스 (WEP에 필요)

int status = WL_IDLE_STATUS;

// WiFi 클라이언트 객체 초기화
WiFiClient client;

// 서버 주소
char server[] = "192.168.0.72";

unsigned long lastConnectionTime = 0; // 마지막 서버 연결 시간 (밀리초)
const unsigned long postingInterval = 10L * 1000L; // 업데이트 간격 (밀리초)
int messageCounter = 0; // 메시지 카운터 초기화

void setup() {
  // 시리얼 통신 초기화
  Serial.begin(9600);
  while (!Serial) {
    ; // 시리얼 포트가 연결될 때까지 대기
  }

  // WiFi 모듈 확인
  if (WiFi.status() == WL_NO_MODULE) {
    Serial.println("Communication with WiFi module failed!");
    while (true); // 계속 대기
  }

  String fv = WiFi.firmwareVersion();
  if (fv < WIFI_FIRMWARE_LATEST_VERSION) {
    Serial.println("Please upgrade the firmware");
  }

  // WiFi 네트워크에 연결 시도
  while (status != WL_CONNECTED) {
    Serial.print("Attempting to connect to SSID: ");
    Serial.println(ssid);
    status = WiFi.begin(ssid, pass); // WPA/WPA2 네트워크에 연결
  }
  printWifiStatus(); // 연결 상태 출력
}

void loop() {
  // 10초가 경과했으면 서버에 다시 연결하여 데이터 전송
  if (millis() - lastConnectionTime > postingInterval) {
    httpRequest();
  }

  // 서버로부터 데이터 수신 및 출력
  read_request();
}

// 서버로부터 데이터 수신 및 시리얼 모니터에 출력
void read_request() {
  while (client.connected() && client.available()) {
    char c = client.read();
    Serial.print(c);
  }
}

// 서버에 HTTP 요청 전송
void httpRequest() {
  client.stop(); // 기존 연결 종료

  if (client.connect(server, 8000)) {
    Serial.println("connecting...");
    String message = "mipmip" + String(messageCounter); // 증가하는 숫자를 포함한 메시지 생성
    client.println(message); // 메시지 전송
    Serial.println("Sent: " + message); // 전송 메시지 출력
    client.println();
    lastConnectionTime = millis(); // 마지막 연결 시간 갱신
    messageCounter++; // 메시지 카운터 증가
  } else {
    Serial.println("connection failed"); // 연결 실패 출력
  }
}

// WiFi 상태 출력
void printWifiStatus() {
  Serial.print("SSID: ");
  Serial.println(WiFi.SSID());

  IPAddress ip = WiFi.localIP();
  Serial.print("IP Address: ");
  Serial.println(ip);

  long rssi = WiFi.RSSI();
  Serial.print("signal strength (RSSI):");
  Serial.print(rssi);
  Serial.println(" dBm");
}
