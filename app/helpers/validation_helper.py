class ValidationHelper:
    def __init__(self, data, options):
        self.options = options
        self.data = data
        self.messages = {}
        self.is_valid = True

    def __del__(self):
        pass

    def valid(self):
        try:
            for key in self.options.keys():
                value = self.data[key] if key in self.data else self.data.get(key)
                if self.options[key].get('required') and (value==None or value == ''):
                    self.messages[key] = "This field cannot be left blank"
                    self.is_valid = False
                else:
                    if self.options[key].get('number'):
                        try:
                            val = int(value)
                            val = float(value)
                        except Exception:
                            self.messages[key] = "This field must be number"
                            self.is_valid = False

            return {
                'is_valid': self.is_valid,
                'messages': self.messages
            }
        except Exception as e:
            return e
