#include <LedControl.h>

const byte NB_MAX7219 = 16;
const byte CS  = 10;
const byte CLK = 11;
const byte DIN = 12;

LedControl lc = LedControl(DIN, CLK, CS, NB_MAX7219);

byte displayBuffer[8 * NB_MAX7219];

const byte alphabet[53][8] = {
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
  {B00011000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000}, /* animation */
  {B00000000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000, B00011000}, 
  {B00011000, B00011000, B00011000, B00011000, B00011000, B00011000, B00011000, B00011000}, 
  {B00111100, B00111100, B00111100, B00111100, B00111100, B00111100, B00111100, B00111100}, 
  {B01111110, B01111110, B01111110, B01111110, B01111110, B01111110, B01111110, B01111110}, 
  {B11111111, B11111111, B11111111, B11111111, B11111111, B11111111, B11111111, B11111111}, 
  {B11100111, B11100111, B11100111, B11100111, B11100111, B11100111, B11100111, B11100111}, 
  {B11000011, B11000011, B11000011, B11000011, B11000011, B11000011, B11000011, B11000011}, 
  {B10000001, B10000001, B10000001, B10000001, B10000001, B10000001, B10000001, B10000001}, /* --------- */
  {B00000000, B00000000, B00111100, B00100000, B00100000, B00100000, B00000000, B00000000}, // L
  {B00000000, B00000000, B00111100, B00000000, B00000000, B00000000, B00111100, B00001000}, // I N
  {B00000000, B00000000, B00000000, B00000000, B00000000, B00000000, B00111100, B00001000}, // N
  {B00010000, B00111100, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000}, // N
  {B00010000, B00111100, B00000000, B00000000, B00111100, B00100000, B00100000, B00111100}, // N U
  {B00000000, B00000000, B00100100, B00011000, B00011000, B00100100, B00000000, B00000000}, // X
  {B11111111, B11111111, B11111111, B11111111, B11111111, B11111111, B11111111, B11111111}, // HIGH
  {B00000000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000}  // space or unknown
};

char msg[27];

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
  } else if ((aChar >= '#') && aChar <= '$') {
    for (int j = 0; j < 8; j++) currentPattern[j] = alphabet[aChar - '#' + 36][j];
  } else for (int j = 0; j < 8; j++) currentPattern[j] = alphabet[52][j];

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
        } else if ((aString[currentChar] >= '#') && (aString[currentChar] <= '$')) {
            for (int j = 0; j < 8; j++) displayBuffer[8 * currentChar + j] = alphabet[aString[currentChar] - '#' + 36][j];
        } else for (int j = 0; j < 8; j++) displayBuffer[8 * currentChar + j] = alphabet[52][j];
      }
    }
    showdisplayBuffer(); delay(scrollSpeed * 4ul);
  }

  while (currentChar < strLength + NB_MAX7219) {
    byte currentPattern[8];
    byte tmpGrid[8];
    // Pause the scrolling if command pause is triggered
    if (Serial.available() != 0) {
      String cmmd = Serial.readString();
      cmmd.toLowerCase();
  
      if (cmmd.length() - 1 == 6) {
        if (cmmd[0] == 'p' && cmmd[1] == 'a' && cmmd[2] == 'u' && cmmd[3] == 's' && cmmd[4] == 'e' && cmmd[5] == '!') {
          while (Serial.available() == 0) {}
          cmmd = Serial.readString();
          cmmd.toLowerCase();
  
          if (cmmd.length() - 1 == 6)
            if (cmmd[0] == 'p' && cmmd[1] == 'a' && cmmd[2] == 'u' && cmmd[3] == 's' && cmmd[4] == 'e' && cmmd[5] == '!') 
              Serial.println("OK!");
        } 
      } 
    }
    
    if (currentChar < strLength) pushChar(aString[currentChar], scrollSpeed);
    else pushChar(' ', scrollSpeed); // Pad with spaces
    currentChar++;
  }
}

void showAnim(int state, boolean resumed) {
  if (Serial.available() != 0 || !resumed) {
    String cmmd = Serial.readString();
    cmmd.toLowerCase();

    if (cmmd.length() - 1 == 6) {
      if (!resumed) {
        if (cmmd[0] == 'p' && cmmd[1] == 'a' && cmmd[2] == 'u' && cmmd[3] == 's' && cmmd[4] == 'e' && cmmd[5] == '!') {
          Serial.println("OK!");
          int s;
          if (state < 14) s = state + 1;
          else s = 0;
          showAnim(s, true);
        } else showAnim(state, false);
      } else if (cmmd[0] == 'p' && cmmd[1] == 'a' && cmmd[2] == 'u' && cmmd[3] == 's' && cmmd[4] == 'e' && cmmd[5] == '!') {
        while (Serial.available() == 0) {}
        cmmd = Serial.readString();
        cmmd.toLowerCase();

        if (cmmd.length() - 1 == 6) {
          if (cmmd[0] == 'p' && cmmd[1] == 'a' && cmmd[2] == 'u' && cmmd[3] == 's' && cmmd[4] == 'e' && cmmd[5] == '!') {
            Serial.println("OK!");
            int s;
            if (state < 14) s = state + 1;
            else s = 0;
            showAnim(s, true);
          } else showAnim(state, false);
        } else showAnim(state, false);
      }
    } 
  }

  if (state == 0) {
    displaySymbol(52, 0);
    displaySymbol(36, 1);
    displaySymbol(37, 2);
    displaySymbol(52, 3);
    delay(1500);
    showAnim(state + 1, true);
  }
  if (state == 1) {
    displaySymbol(38, 0);
    displaySymbol(38, 1);
    displaySymbol(38, 2);
    displaySymbol(38, 3);
    delay(100);
    showAnim(state + 1, true);
  }
  if (state == 2) {
    displaySymbol(39, 0);
    displaySymbol(39, 1);
    displaySymbol(39, 2);
    displaySymbol(39, 3);
    delay(100);
    showAnim(state + 1, true);
  }
  if (state == 3) {
    displaySymbol(40, 0);
    displaySymbol(40, 1);
    displaySymbol(40, 2);
    displaySymbol(40, 3);
    delay(100);
    showAnim(state + 1, true);
  }
  if (state == 4) {
    displaySymbol(41, 0);
    displaySymbol(41, 1);
    displaySymbol(41, 2);
    displaySymbol(41, 3);
    delay(100);
    showAnim(state + 1, true);
  }
  if (state == 5) {
    displaySymbol(42, 0);
    displaySymbol(42, 1);
    displaySymbol(42, 2);
    displaySymbol(42, 3);
    delay(100);
    showAnim(state + 1, true);
  }
  if (state == 6) {
    displaySymbol(43, 0);
    displaySymbol(43, 1);
    displaySymbol(43, 2);
    displaySymbol(43, 3);
    delay(100);
    showAnim(state + 1, true);
  }
  if (state == 7) {
    displaySymbol(44, 0);
    displaySymbol(44, 1);
    displaySymbol(44, 2);
    displaySymbol(44, 3);
    delay(100);
    showAnim(state + 1, true);
  }
  if (state == 8) {
    displaySymbol(52, 0);
    displaySymbol(52, 1);
    displaySymbol(52, 2);
    displaySymbol(52, 3);
    delay(500);
    showAnim(state + 1, true);
  }
  if (state == 9) {
    displaySymbol(45, 3);
    delay(500);
    showAnim(state + 1, true);
  }
  if (state == 10) {
    displaySymbol(50, 0);
    delay(500);
    showAnim(state + 1, true);
  }
  if (state == 11) {
    displaySymbol(48, 1);
    displaySymbol(47, 2);
    delay(500);
    showAnim(state + 1, true);
  }
  if (state == 12) {
    displaySymbol(49, 1);
    delay(500);
    showAnim(state + 1, true);
  }
  if (state == 13) {
    displaySymbol(46, 2);
    delay(2000);
    showAnim(state + 1, true);
  }
  if (state == 14) {
    displaySymbol(52, 0);
    displaySymbol(52, 1);
    displaySymbol(52, 2);
    displaySymbol(52, 3);
    showAnim(0, true);
  }
}

void readCmmd(String cmmd) {
  if (cmmd.length() - 1 == 8) {
    if (cmmd[0] == 'c' && cmmd[1] == 'o' && cmmd[2] == 'n' && cmmd[3] == 't' && cmmd[4] == 'r' && cmmd[5] == 'o' && cmmd[6] == 'l' && cmmd[7] == '!') {
      while (Serial.available() == 0) {}
      cmmd = Serial.readString(); 
      cmmd.toLowerCase();

      if (cmmd.length() - 1 == 8) {
        if (cmmd[0] == 'c' && cmmd[1] == 'o' && cmmd[2] == 'n' && cmmd[3] == 't' && cmmd[4] == 'r' && cmmd[5] == 'o' && cmmd[6] == 'l' && cmmd[7] == '!') 
          readCmmd(cmmd);
      } else if (cmmd.length() - 1 == 6) {
        if (cmmd[0] == 'w' && cmmd[1] == 'r' && cmmd[2] == 'i' && cmmd[3] == 't' && cmmd[4] == 'e' && cmmd[5] == '!') {
          while (Serial.available() == 0) {}
          String msg_tmp = "                ";
          msg_tmp += Serial.readString(); 
          if (msg_tmp[msg_tmp.length() - 2] == '*') {
            msg_tmp = msg_tmp.substring(0, msg_tmp.length() - 2);
            msg_tmp.toCharArray(msg, 27);  
            Serial.println("OK!");
          }
        } else if (cmmd[0] == 'b' && cmmd[1] == 'l' && cmmd[2] == 'a' && cmmd[3] == 'n' && cmmd[4] == 'k' && cmmd[5] == '!') {
          displaySymbol(51, 0);
          displaySymbol(51, 1);
          displaySymbol(51, 2);
          displaySymbol(51, 3);
          Serial.println("OK!");
        } else if (cmmd[0] == 'p' && cmmd[1] == 'a' && cmmd[2] == 'u' && cmmd[3] == 's' && cmmd[4] == 'e' && cmmd[5] == '!') {
          while (Serial.available() == 0) {}
          cmmd = Serial.readString(); 
          cmmd.toLowerCase();

          if (cmmd[0] == 'p' && cmmd[1] == 'a' && cmmd[2] == 'u' && cmmd[3] == 's' && cmmd[4] == 'e' && cmmd[5] == '!') 
            Serial.println("OK!"); 
        }
      } else if (cmmd.length() - 1 == 5) {
        if (cmmd[0] == 's' && cmmd[1] == 'h' && cmmd[2] == 'o' && cmmd[3] == 'w' && cmmd[4] == '!') {
          displaySymbol(52, 0);
          displaySymbol(52, 1);
          displaySymbol(52, 2);
          displaySymbol(52, 3);
          Serial.println("OK!");
          scrollTxt(msg, 50ul, true);
        } else if (cmmd[0] == 'l' && cmmd[1] == 'o' && cmmd[2] == 'g' && cmmd[3] == 'o' && cmmd[4] == '!') {
          displaySymbol(52, 0);
          displaySymbol(52, 1);
          displaySymbol(52, 2);
          displaySymbol(52, 3);
          Serial.println("OK!");
          showAnim(0, true);
        }
      } 
    } 
  } 
}

void setup() {
  Serial.begin(9600);
  String init_msg = "                Lorem here";
  init_msg.toCharArray(msg, 27);
  
  for (int index = 0; index < NB_MAX7219; index++) { // NB_MAX7219 similar to lc.getDeviceCount()
    lc.shutdown(index, false);
    lc.setIntensity(index, 4); // (0~15)
    lc.clearDisplay(index);
  }
}

void loop() {
  while (Serial.available() == 0) {}
  String command = Serial.readString(); 
  command.toLowerCase();
  readCmmd(command);
}
