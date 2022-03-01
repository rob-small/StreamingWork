# StreamingWork
 
# Running Loki
(base) osboxes@osboxes:~$ cd loki
(base) osboxes@osboxes:~/loki$ ./loki-linux-amd64 -config.file=loki-local-config.yaml

# See Loki running
http://localhost:3100/metrics

# Running Promtail
(base) osboxes@osboxes:~$ cd loki
(base) osboxes@osboxes:~/loki$ ./promtail-linux-amd64 -config.file=promtail-local-config.yaml

# Running Grafana
sudo systemctl daemon-reload
sudo systemctl start grafana-server
sudo systemctl status grafana-server

# See Grafana running
http://localhost:3000/

# Setup logging for StreamingWork
sudo mkdir /var/log/streamingwork
sudo chmod a+w /var/log/streamingwork
osboxes@osboxes:~/github/StreamingWork$ python device-generator.py > /var/log/streamingwork/out.log
