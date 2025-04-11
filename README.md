# BreadBot

[![Made With](https://img.shields.io/badge/Made%20With-Micropython-<COLOR>.svg)](https://shields.io/)  [![Project Status](https://img.shields.io/badge/Status-Alpha-orange)](https://shields.io/)   ![License](https://img.shields.io/github/license/skyriderdragoon/BreadBotPico)


---

BreadBot is a project designed to automate the development of bread dough.

---

## Features

- Automates repetitive tasks.
- Provides an intuitive interface for users.
- Extensible and customizable.
<details>
<summary>Show Planned</summary>
    
- MQTT Integration
- Mobile Notifications
</details>

## Getting Started
1. Clone the repository:
    ```bash
    git clone https://github.com/skyriderdragoon/BreadBot.git
    ```
2. Navigate to the project directory:
    ```bash
    cd BreadBot
    ```
3. Install dependencies (if applicable).
>[!IMPORTANT]
>4. Populate the default secrets.py with the following variables
```python
        SSID = "Your WiFi SSID"
        PASS = "Your WiFi Password"
        MQTT_USER = "Your MQTT Broker Username"
        MQTT_PASS = "Your MQTT Broker Password"
        MQTT_SERV = "Your MQTT Broker Server Address"
```
## Current Hardware
- Raspberry Pi Pico W with Micropython 1.23 (with pimoroni libraries)
- Pimoroni VL53L5CX
- 2x LED
    - 1x Red
    - 1x Green

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the GNU General Public License v3.0. See the `LICENSE` file for details.

## Contact

For questions or feedback, please contact [breadbot@danielrobertson.info].

## Contact

For questions or feedback, please contact [breadbot@danielrobertson.info].

### Copyright 2025 Daniel Robertson (Killer Wing Designs)
