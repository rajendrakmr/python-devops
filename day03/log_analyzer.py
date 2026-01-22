import json


class logAnalyzer: 
    def __init__(self,file_name,output_file):
        self.file_name = file_name
        self.output_file = output_file 

    def read_logs(self):
        # file = open(file)
        # print(file.read())
        # file.close()
        line = []
        with open(self.file_name,"r") as shu:
            # print(shu.readlines())
            return shu.readlines()
            # return line.append(shu.readlines())

        # return line
        


    
    def analyzer(self):
        lines = self.read_logs()
        log_count ={
            "authenticaton_failure":0,
            "check_user_unknown":0,
            "alert":0
        }
        for line in lines:
            if "authentication failure" in line:
                log_count.update({ "authenticaton_failure":log_count["authenticaton_failure"]+1})
            elif "check pass; user unknown" in line:
                log_count.update({"check_user_unknown":log_count["check_user_unknown"]+1}) 
            elif "ALERT" in line:
                log_count.update({"alert":log_count["alert"]+1}) 
        print('total authentication failure count ',log_count)
        return log_count


   
    def write_json(self):
        counts = self.analyzer()
        with open(self.output_file,"+w") as jsonfile:
            json.dump(counts,jsonfile)





log = logAnalyzer("app.log","ouput.json") # creating object
log.analyzer()
log.write_json()
#  logs_count = analyzer(log_data)

# log_data = read_logs('app.log')

# write_json(logs_count)