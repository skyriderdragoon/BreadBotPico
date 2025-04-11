# BreadBot

BreadBot is a project designed to automate the development of bread dough.

## Features

- Automates repetitive tasks.
- Provides an intuitive interface for users.
- Extensible and customizable.

## Getting Started

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/BreadBot.git
    ```
2. Navigate to the project directory:
    ```bash
    cd BreadBot
    ```
3. Install dependencies (if applicable).
4. Populate the default secrets.py with the following variables
    ```
        SSID = "Your WiFi SSID"
        PASS = "Your WiFi Password"
        MQTT_USER = "Your MQTT Broker Username"
        MQTT_PASS = "Your MQTT Broker Password"
        MQTT_SERV = "Your MQTT Broker Server Address"
    ```

## Current Tech
- Raspberry Pi Pico W with Micropython 1.23 (with pimoroni libraries)
- Pimoroni VL53L5CX
- 2x LED
    - 1x Red
    - 1x Green

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For questions or feedback, please contact [breadbot@danielrobertson.info].

Copyright 2025 Daniel Robertson (Killer Wing Designs)