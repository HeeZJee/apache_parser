
from modules.log_formatter import format_logs
from src.count_path import count_path
from src.count_code_except import count_code_except
from src.count_path_with_method import count_path_with_method
from src.count_ip import count_ip


if __name__ == "__main__":
    path = count_path("/production/file_metadata/modules/ssh/sshd_config?")
    code_expect_200 = count_code_except('200')
    path_with_method = count_path_with_method("/dev/report/", "PUT")
    count_ip = count_ip()
    
      
    print(f"How many times the URL '/production/file_metadata/modules/ssh/sshd_config' was fetched? \n{path}\n")
    print(f"Of those requests, how many times the return code from Apache was not 200? \n{code_expect_200}\n")
    print(f"The total number of times Apache returned any code other than 200? \n{code_expect_200}\n")
    print(f"The total number of times that any IP address sent a PUT request to a path under '/dev/report/'? \n{path_with_method}\n")
    print(f"A breakdown of how many times such requests were made by IP address? \n{count_ip}")