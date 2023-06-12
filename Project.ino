#include <LedControl.h>

const byte NB_MAX7219 = 16;
const byte CS = 10;
const byte CLK = 11;
const byte DIN = 12;

LedControl lc = LedControl(DIN, CLK, CS, NB_MAX7219);

byte displayBuffer[8 * NB_MAX7219];

const byte alphabet[40][8] = {
  {B00000000, B00111000, B01000100, B01001100, B01010100, B01100100, B01000100, B00111000}, // 0
  {B00000000, B00010000, B00110000, B00010000, B00010000, B00010000, B00010000, B00111000}, // 1
  {B00000000, B00111000, B01000100, B00000100, B00001000, B00010000, B00100000, B01111100}, // 2
  {B00000000, B01111100, B00001000, B00010000, B00001000, B00000100, B01000100, B00111000}, // 3
  {B00000000, B00001000, B00011000, B00101000, B01001000, B01111100, B00001000, B00001000}, // 4
  {B00000000, B01111100, B01000000, B01111000, B00000100, B00000100, B01000100, B00111000}, // 5
  {B00000000, B00011000, B00100000, B01000000, B01111000, B01000100, B01000100, B00111000}, // 6
  {B00000000, B01111100, B00000100, B00001000, B00010000, B00100000, B01000000, B01000000}, // 7
  {B00000000, B00111000, B01000100, B01000100, B00111000, B01000100, B01000100, B00111000}, // 8
  {B00000000, B00111000, B01000100, B01000100, B00111100, B00000100, B00001000, B00110000}, // 9
  {B00000000, B00111000, B01000100, B01000100, B01111100, B01000100, B01000100, B01000100}, // A
  {B00000000, B01111000, B01000100, B01000100, B01111000, B01000100, B01000100, B01111000}, // B
  {B00000000, B00111000, B01000100, B01000000, B01000000, B01000000, B01000100, B00111000}, // C
  {B00000000, B01111000, B01000100, B01000100, B01000100, B01000100, B01000100, B01111000}, // D
  {B00000000, B01111100, B01000000, B01000000, B01111000, B01000000, B01000000, B01111100}, // E
  {B00000000, B01111100, B01000000, B01000000, B01111000, B01000000, B01000000, B01000000}, // F
  {B00000000, B00111000, B01000100, B01000000, B01000000, B01001100, B01000100, B00111000}, // G
  {B00000000, B01000100, B01000100, B01000100, B01111100, B01000100, B01000100, B01000100}, // H
  {B00000000, B00111000, B00010000, B00010000, B00010000, B00010000, B00010000, B00111000}, // I
  {B00000000, B00011100, B00001000, B00001000, B00001000, B00001000, B01001000, B00110000}, // J
  {B00000000, B01000100, B01001000, B01010000, B01100000, B01010000, B01001000, B01000100}, // K
  {B00000000, B01000000, B01000000, B01000000, B01000000, B01000000, B01000000, B01111000}, // L
  {B00000000, B01000100, B01101100, B01010100, B01010100, B01000100, B01000100, B01000100}, // M
  {B00000000, B01000100, B01000100, B01100100, B01010100, B01001100, B01000100, B01000100}, // N
  {B00000000, B00111000, B01000100, B01000100, B01000100, B01000100, B01000100, B00111000}, // O
  {B00000000, B01111000, B01000100, B01000100, B01111000, B01000000, B01000000, B01000000}, // P
  {B00000000, B00111000, B01000100, B01000100, B01000100, B01010100, B01001000, B00110100}, // Q
  {B00000000, B01111000, B01000100, B01000100, B01111000, B01010000, B01001000, B01000100}, // R
  {B00000000, B00111100, B01000000, B01000000, B00111000, B00000100, B00000100, B01111000}, // S
  {B00000000, B01111100, B00010000, B00010000, B00010000, B00010000, B00010000, B00010000}, // T
  {B00000000, B01000100, B01000100, B01000100, B01000100, B01000100, B01000100, B00111000}, // U
  {B00000000, B01000100, B01000100, B01000100, B01000100, B00101000, B00101000, B00010000}, // V
  {B00000000, B01000100, B01000100, B01000100, B01010100, B01010100, B01010100, B00101000}, // W
  {B00000000, B01000100, B01000100, B00101000, B00010000, B00101000, B01000100, B01000100}, // X
  {B00000000, B01000100, B01000100, B00101000, B00010000, B00010000, B00010000, B00010000}, // Y
  {B00000000, B01111100, B00000100, B00001000, B00010000, B00100000, B01000000, B01111100}, // Z
  {B00000000, B00000000, B00000000, B00000000, B00000000, B00000000, B00011000, B00011000}, // ., 36
  {B00000000, B00000110, B00000110, B00000000, B00000000, B00000000, B00000000, B00000000}, // °, 37
  {B00000000, B01100010, B01100100, B00001000, B00010000, B00100110, B01000110, B00000000}, // %, 38
  {B00000000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000}  // space or unknown
};

void displaySymbol(int charNb, byte n) {
  for (int lineNb = 0; lineNb < 8; lineNb++)
    lc.setRow(n, lineNb, alphabet[charNb][lineNb]);
}

void showdisplayBuffer() {
  for (int n = 0; n < NB_MAX7219; n++) {
    for (int l = 0; l < 8; l++)
      lc.setRow(NB_MAX7219 - 1 - n, l, displayBuffer[8 * n + l]);
  }
}

void pushChar(const char aChar, unsigned long scrollSpeed) {
  byte currentPattern[8];
  byte tmpGrid[8];

  if ((aChar >= '0') && (aChar <= '9')) {
    for (int j = 0; j < 8; j++) currentPattern[j] = alphabet[aChar - '0'][j];
  } else if ((toupper(aChar) >= 'A') && (toupper(aChar) <= 'Z')) {
      for (int j = 0; j < 8; j++) currentPattern[j] = alphabet[toupper(aChar) - 'A' + 10][j];
  } else if (aChar == '.') {
    for (int j = 0; j < 8; j++) currentPattern[j] = alphabet[aChar - '.' + 36][j];
  } else if (aChar == ':') {
    for (int j = 0; j < 8; j++) currentPattern[j] = alphabet[aChar - ':' + 37][j];
  } else if (aChar == '%') {
    for (int j = 0; j < 8; j++) currentPattern[j] = alphabet[aChar - '%' + 38][j];
  } else for (int j = 0; j < 8; j++) currentPattern[j] = alphabet[39][j];

  memset (tmpGrid, 0, sizeof(tmpGrid));
  for (byte r = 0; r < 8; r++)
    for (byte b = 0; b < 8; b++)
      if (bitRead(currentPattern[b], r)) bitSet(tmpGrid[7 - r], b);
  for (byte r = 0; r < 8; r++) currentPattern[r] = tmpGrid[r];

  for (byte r = 0; r < 8; r++) {
    for (int l = 1; l < 8 * NB_MAX7219; l++) displayBuffer[l - 1] = displayBuffer[l];
    displayBuffer[8 * NB_MAX7219 - 1] = currentPattern[r];
    showdisplayBuffer(); delay(scrollSpeed);
  }
}

void scrollTxt(const char * aString, unsigned long scrollSpeed, bool preloadDisplay) {
  int strLength = strlen(aString);
  int currentChar = 0;

  memset (displayBuffer, 0, sizeof(displayBuffer));
  if (preloadDisplay) {
    // Preload the display
    for (currentChar = 0; currentChar < NB_MAX7219; currentChar++) {
      if (currentChar < strLength) {
        if ((aString[currentChar] >= '0') && (aString[currentChar] <= '9')) {
          for (int j = 0; j < 8; j++) displayBuffer[8 * currentChar + j] = alphabet[aString[currentChar] - '0'][j];
        } else if ((toupper(aString[currentChar]) >= 'A') && (toupper(aString[currentChar]) <= 'Z')) {
            for (int j = 0; j < 8; j++) displayBuffer[8 * currentChar + j] = alphabet[toupper(aString[currentChar]) - 'A' + 10][j];
        } else if (aString[currentChar] == '.') {
            for (int j = 0; j < 8; j++) displayBuffer[8 * currentChar + j] = alphabet[aString[currentChar] - '.' + 36][j];
        } else if (aString[currentChar] == ':') {
            for (int j = 0; j < 8; j++) displayBuffer[8 * currentChar + j] = alphabet[aString[currentChar] - ':' + 37][j];
        } else if (aString[currentChar] == '%') {
            for (int j = 0; j < 8; j++) displayBuffer[8 * currentChar + j] = alphabet[aString[currentChar] - '%' + 38][j];
        } else for (int j = 0; j < 8; j++) displayBuffer[8 * currentChar + j] = alphabet[39][j];
      }
    }
    showdisplayBuffer(); delay(scrollSpeed * 4ul);
  }

  while (currentChar < strLength + NB_MAX7219) {
    byte currentPattern[8];
    byte tmpGrid[8];
    if ( currentChar < strLength) pushChar(aString[currentChar], scrollSpeed);
    else pushChar(' ', scrollSpeed); // Pad with spaces
    currentChar++;
  }
}

void setup() {
  Serial.begin(9600);
  for (int index = 0; index < NB_MAX7219; index++) { // NB_MAX7219 similar to lc.getDeviceCount()
    lc.shutdown(index, false);
    lc.setIntensity(index, 4); // (0~15)
    lc.clearDisplay(index);
  }
}

void loop() {
  const char message[] = "";

  while(Serial.available()) {
    String msg_tmp = "                ";
    String received = Serial.readString();
    
    if (received.length() > 0) {
      char pause = received[0];
      if (pause == '0') {
        received = received.substring(2, received.length());
        msg_tmp += received;
        msg_tmp.toCharArray(message, 27); 
        scrollTxt(message, 50ul, true);
        delay(2500);
      }
      Serial.end();
      Serial.begin(9600);
    }
  }
}
