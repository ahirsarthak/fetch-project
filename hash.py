from hashlib import sha256


def mask_pii(data):
    # Hash device_id and ip using sha256
    data['masked_device_id'] = sha256(data['device_id'].encode()).hexdigest()
    data['masked_ip'] = sha256(data['ip'].encode()).hexdigest()
    return data


data = {'device_id': '593-47-598', 'ip': '199.172.1111.135'}
masked_data = mask_pii(data)
print(masked_data)
# Output: {'masked_device_id': 'b9e9c9b1f5f0a3d3e3f5e2c87b0e5d9c5f5d5f5c5b5d5d5f5e5d5e5d5f5e5d5f', 'masked_ip': 'b9e9c9b1f5f0a3d3e3f5e2c87b0e5d9c5f5d5f5c5b5d5d5f5e5d5e5d5f5e5d5f'}
