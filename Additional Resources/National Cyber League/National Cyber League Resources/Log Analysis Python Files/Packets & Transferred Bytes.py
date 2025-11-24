"""
This is the following information answered by this file. 
* Q1: Number of unique IP addresses: 141
* Q2: Time elapsed between first and last packets (in ms): 48897
* Q3: Number of UDP packets: 3046
* Q4: Total bytes transferred: 16415555
* Q5: Total bytes sent by 146.75.33.44: 27994
* Q6: IP addresses that responded to a ping: ['146.75.37.140' '146.75.29.140' '146.75.30.133' '146.75.34.137' '146.75.38.133' '104.18.34.200' '146.75.33.44' '162.19.138.118' '23.220.124.15' '96.7.19.48' '35.71.139.29' '146.75.32.193' '146.75.29.44' '172.64.149.180' '141.226.124.48' '216.223.26.41' '141.226.224.48' '52.54.149.30' '34.98.64.218']
* Q7: IP address pair with the largest network traffic: 146.75.29.140 <> 192.168.29.130
"""

import pandas as pd

# Load the CSV file
packets = pd.read_csv("packets.csv")

# Q1: Number of unique IP addresses
unique_ips = pd.concat([packets['src_ip'], packets['dst_ip']]).nunique()

# Q2: Time elapsed in milliseconds between the first and last packets
time_elapsed = int(packets['timestamp'].max() - packets['timestamp'].min())

# Q3: Number of UDP packets
udp_count = packets[packets['transport_proto'] == 'UDP'].shape[0]

# Q4: Total bytes transferred
total_bytes_transferred = packets['bytes_transferred'].sum()

# Q5: Total bytes sent by 146.75.33.44 (exclude received packets)
bytes_sent_by_ip = packets[packets['src_ip'] == '146.75.33.44']['bytes_transferred'].sum()

# Q6: IP address that responded to a ping
# Assuming "ping response" means packets where ICMP packets are present with an IP as the destination
ping_responders = packets[packets['tcp_flags'] == 'R']['dst_ip'].unique()

# Q7: IP address pair with the largest network traffic
# Group by src-dst pairs and sum bytes transferred to find the largest
packets['ip_pair'] = packets.apply(lambda x: tuple(sorted([x['src_ip'], x['dst_ip']])), axis=1)
traffic_by_pair = packets.groupby('ip_pair')['bytes_transferred'].sum()
largest_traffic_pair = traffic_by_pair.idxmax()

# Displaying the results
print("Q1: Number of unique IP addresses:", unique_ips)
print("Q2: Time elapsed between first and last packets (in ms):", time_elapsed)
print("Q3: Number of UDP packets:", udp_count)
print("Q4: Total bytes transferred:", total_bytes_transferred)
print("Q5: Total bytes sent by 146.75.33.44:", bytes_sent_by_ip)
print("Q6: IP addresses that responded to a ping:", ping_responders)
print("Q7: IP address pair with the largest network traffic:", f"{largest_traffic_pair[0]} <> {largest_traffic_pair[1]}")
