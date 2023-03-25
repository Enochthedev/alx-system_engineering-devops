# Web infrastructure design
After looking through the project this I began to research web infrastructure design
and this was the outcome
To design a one-server web infrastructure that hosts the website reachable via www.foobar.com, we can use the following setup:

Server: We will use a single physical server to host the entire web infrastructure.
Web server: Nginx will be used as the web server to handle incoming requests from the user.
Application server: We will use an application server such as Gunicorn or uWSGI to run the application code.
Application files: The code base for the website will be stored on the server.
Database: We will use MySQL as the database server to store and manage website data.
Domain name: The domain name foobar.com will be registered and configured with a www record that points to the server IP 8.8.8.8.
When a user wants to access the website, they will enter www.foobar.com into their web browser. The browser will send a request to the DNS server to resolve the domain name to an IP address. The DNS server will return the IP address 8.8.8.8, which is the server's IP address.

The request will then be sent to the web server (Nginx) on the server. Nginx will handle the request and pass it on to the application server (Gunicorn or uWSGI), which will run the website's code and generate a response. The response will be sent back to Nginx, which will return it to the user's browser.

The server acts as a central point of failure (SPOF) in this infrastructure. If the server goes down, the entire website will be inaccessible. Additionally, when performing maintenance, such as deploying new code or restarting the web server, the website will experience downtime. Finally, if the website receives too much incoming traffic, it cannot scale to handle it effectively.

To address these issues, we can consider implementing load balancing, using a distributed file system, and/or adding additional servers to handle traffic spikes.

URLs:

Nginx: https://nginx.org/
Gunicorn: https://gunicorn.org/
uWSGI: https://uwsgi-docs.readthedocs.io/en/latest/
MySQL: https://www.mysql.com/
DNS: https://en.wikipedia.org/wiki/Domain_Name_System