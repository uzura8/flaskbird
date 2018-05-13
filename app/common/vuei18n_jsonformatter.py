import os, json, re

class VueI18nJsonFormatter():
    def __init__(self, input_file, output_dir, option={}):
        self.input_file = input_file
        self.output_dir = output_dir.rstrip('/')
        self.output_file = ''
        self.json_dict = {}
        self.formatted = {}
        self.json_format = {
            'indent': 4,
            'sort_keys': True,
            'separators':(',', ': ')
        }
        self.lang = ''
        self.group = ''

        self.init_en = False
        if 'init_en' in option:
            self.init_en = option['init_en']

    def execute(self):
        self.set_prop()
        self.load()
        self.format()
        self.output()

    def format(self):
        dict_new = {}
        for key, values in self.json_dict.items():
            if len(key) == 0 or len(values) < 2:
                continue
            key = self.conv_delimitter(key)
            if self.init_en:
                value = key
            else:
                value = self.conv_delimitter(values[1])
            dict_new[key] = value
        self.formatted = {self.group: dict_new}

    def set_prop(self):
        input_filename = os.path.basename(self.input_file)
        m = re.search('^([a-z_]+)-([a-z_]+)\.json$', input_filename)
        self.lang = m.group(1) if not self.init_en else 'en'
        self.group = m.group(2)
        self.output_file = '{}/{}-{}.json'.format(self.output_dir,
                                                self.lang, self.group)

    @staticmethod
    def conv_delimitter(src):
        return re.sub(r'%\((\w+)\)s', r'{\1}', src)

    def load(self):
        with open(self.input_file, 'r') as f:
            self.json_dict = json.load(f)

    def set_output_file(self):
        pass

    def output(self):
        with open(self.output_file, 'w') as f:
            json.dump(self.formatted, f,
                    indent=self.json_format['indent'],
                    sort_keys=self.json_format['sort_keys'],
                    separators=self.json_format['separators'])
