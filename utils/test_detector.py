from detector import detect_attack

# Sample input
result = detect_attack(packet_rate=1000, src_ip_count=20, dst_port=80, protocol_str="TCP")
print(result)
