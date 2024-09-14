# Overview:

This repository sets up a Docker-based environment for routing multiple media-related containers through a central VPN
proxy. The setup ensures that all media-related traffic is securely routed through the VPN, while maintaining separate
containers for each service. This repo is largely based on the snippet found
here: https://gist.github.com/vnl/ba6618f56f15bbaea7ac862a3a6a617e

# Prerequisites:

Make sure the following are installed:

* Docker
* Docker Compose

# How to Use:

1. Clone the repository

    ```bash
    git clone https://github.com/adityakunapuli/media-proxy-hub.git
    cd media-proxy-hub
    ```

2. Configure your environment

   Ensure your `.env` file is setup as follows (or rename `EXAMPLE.env` to `.env`)
    ```dotenv
    VPN_SERVICE_PROVIDER=ipvanish
    SERVER_COUNTRIES="United States"
    TZ=America/Los_Angeles
    OPENVPN_USERNAME=<your openvpn username>
    OPENVPN_PASSWORD=<your openvpn password>
    ```
    Additionally you can set the password for qbt using the `create_qbt_password.py` script.
3. Start the services

    ```bash
    docker-compose up -d
    ```
4. Access the services: check `nginx.conf` file in `config/nginx/nginx.conf` for the paths to the various services.
5. Note that you can ensure that your traffic is correctly routed through the VPN using this
   site: https://www.whatismyip.net/tools/torrent-ip-checker/





