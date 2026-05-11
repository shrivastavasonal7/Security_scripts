#Scan target IP for open/closed/filtered ports with service detection
import socket

common_services = {
    22: "SSH",
    80:"HTTP",
    443:"HTTPS",
    3306:"MySQL",
    3389:"RDP",
    8080:"HTTP-ALT",
    6379:"Redis",
}

def scan_ports(target_ip, ports):
    open_ports = []
    print(f"Scanning {target_ip} for ports: {ports}")
    for port in ports:
            service = common_services.get(port,"Unknown service")
            try:
                  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
                        s.settimeout(1) #if no response in 1 second, consider it closed/filtered
                        s.connect((target_ip, port))
                        print(f"port {port} is open ({service})")
                        open_ports.append(port)

            except (socket.timeout, ConnectionRefusedError):
                  print(f"port {port} is closed/filtered ({service})")
    
    return open_ports      

if __name__ == "__main__":
      target_ip = "127.0.0.1"
      ports = [22, 80, 443, 3306, 3389, 8080, 6379]
      results = scan_ports(target_ip, ports)
      print(f"\nOpen ports found: {results}")


