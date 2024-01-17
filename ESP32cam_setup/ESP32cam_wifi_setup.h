/*
 * wifi_setup.h
 *
 *  Created on: Oct 12, 2023
 *      Author: Huy Ly
 */

#ifndef INC_WIFI_SETUP_H_
#define INC_WIFI_SETUP_H_

#include "esp_camera.h"
#include <WiFi.h>
#include <Arduino.h>
#include <EEPROM.h>
// WARNING!!! PSRAM IC required for UXGA resolution and high JPEG quality
//            Ensure ESP32 Wrover Module or other board with PSRAM is selected
//            Partial images will be transmitted if image exceeds buffer size
//
//            You must select partition scheme from the board menu that has at least 3MB APP space.
//            Face Recognition is DISABLED for ESP32 and ESP32-S2, because it takes up from 15 
//            seconds to process single frame. Face Detection is ENABLED if PSRAM is enabled as well
// ===================
// Select camera model
// ===================
#define CAMERA_MODEL_AI_THINKER // Has PSRAM
#include "camera_pins.h"
#include <Preferences.h>

class Wifi_esp32 {
  private:
    Preferences preferences; 
    String ssid;
    String password;

  private:
    void saveWifiCredentials(String, String); // Lưu trữ ssid và password wifi
    bool check_savedWifi(); // Kiểm tra wifi có lưu hay chưa, nếu chưa sẽ smartconfig
    void setupSmartConfig(); // Chạy smartconfig
    void printSuccess(); // In kết quả thành công
    void flashing_led(int, int); // Hàm để chớp tắt led
  public:
    Wifi_esp32(); 
    Wifi_esp32(String, String);
    void setupWifi(); // Chỉ gọi duy nhất hàm này trong chương trình chính
};

#endif /* INC_WIFI_SETUP_H_ */
