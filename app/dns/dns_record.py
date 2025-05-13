class DNSRecord:
    def __init__(self, name, type, ttl, data):
        self.name = name
        self.type = type
        self.ttl = ttl
        self.data = data

    def __str__(self):
        return f"[name: {self.name}, type={self.type} ttl={self.ttl} data={self.data}]"