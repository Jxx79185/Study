def create_logger(prefix):
    def logger(message):
        print(f"[{prefix}] {message}")  # 捕获外部变量 prefix
    return logger

error_log = create_logger("ERROR")
info_log = create_logger("INFO")
error_log("Something wrong!")  # [ERROR] Something wrong!
info_log("Process started.")   # [INFO] Process started.

#对外部变量进行保留和冻结，在需要的时候来进行使用






