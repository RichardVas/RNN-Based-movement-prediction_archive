import json


class Configuration:
    def __init__(self, filename):
        self.filename= filename

        self.pre_trained = None,
        self.trained_model = None,
        self.dataset = None,
        self.stream = None,
        self.evaluation_mode = None,

        self.test = None,
        self.parse_file()
    def parse_file(self):
        #content = {}
        try:
            file = open(self.filename)
            content = json.load(file)
            for i in content:
                print(i)
                print(content[i])
                self.pre_trained =  content['pre_trained']
                self.trained_model = content['trained_model']
                self.dataset  = content['dataset']
                self.stream   = content['stream']
                self.evaluation_mode  =  content['evaluation_mode']
                self.test = content['test']
            file.close()

         #   print(content)
           # return content
        except FileNotFoundError:
            print('The given file named "{}" cannot be found'.format(self.filename))
        except KeyError as error:
            print('Missing value in JSON file at {}'.format(error.args))

config = Configuration('config.json')
#config.parse_file()

