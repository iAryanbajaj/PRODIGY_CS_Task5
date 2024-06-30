from scapy.all import sniff, get_if_list
import platform

# Choose interface to capture from
def choose_interface():
    if platform.system() == "Windows":
        interfaces = get_windows_if_list()
    else:
        interfaces = get_if_list()

    print("Available network interfaces: \n")
    for i, interface in enumerate(interfaces):
        print(f"{i + 1}. {interface['name'] if platform.system() == 'Windows' else interface}")
    
    index_interface = int(input("Select the number of the interface you want to capture from: "))
    return interfaces[index_interface - 1]['name'] if platform.system() == 'Windows' else interfaces[index_interface - 1]

# Packet sniffing
def sniff_packets(interface):
    packets = sniff(iface=interface, count=5)
    if packets:
        return packets
    else:
        print("No packets captured from interface:", interface)
        return None

# Analyze packets
def packet_analyze(packets):
    for packet in packets:
        print("Original packet:", packet)
        print("Packet summary:", packet.summary())

if __name__ == "__main__":
    print("Ethical Considerations: Ensure you have explicit permission to capture network traffic.")
    
    interface = choose_interface()
    packets_captured = sniff_packets(interface)
    if packets_captured:
        print("Packet details:\n")
        packet_analyze(packets_captured)
