from Core.Elena.Tools.VTools import array_key_exists
class GateWay:
    @staticmethod
    def RoutingCore(user_route: str, get_route: str, mode: bool = False):
        user_route = user_route.strip().replace("/", ",").replace("\\", ",").split(",")
        get_route = get_route.strip().replace("/", ",").replace("\\", ",").split(",")

        param_read_flag = False
        param_read_count = 2
        param_read_max = 0
        param_key = ""
        uri_params = list()
        i = 0
        ri = 0

        while(True):
            if(len(user_route) > i):
                if(i == 0 and i in get_route):
                    i += 1
                elif(array_key_exists(ri, user_route) and "@" in user_route[ri] and array_key_exists(i, get_route) and not param_read_flag or mode and param_read_flag):
                    param_check = user_route[ri].lstrip("@")
                    param_read = param_check.split(":")
                    if(param_check != "" and len(param_read) >= 1):
                        uri_params.append(get_route[i])
                        if(param_read[1].isdigit):
                            param_read_max = int(param_read[1])
                        else:
                            param_read_max = 20
                    else:
                        return False

                    param_read_flag = True
                    i += 1
                    ri += 1

                elif(array_key_exists(ri, user_route) and ":" in user_route[ri] and array_key_exists(i, get_route) and not param_read_flag or mode and not param_read_flag):
                    uri_params[user_route[ri].lstrip(":")] = get_route[i]
                    i += 1
                    ri += 1

                elif(array_key_exists(ri, user_route) and "{" in user_route[ri] and "}" in user_route[ri] and array_key_exists(i, get_route) and not param_read_flag or mode and not param_read_flag):
                    param_check = user_route[ri].strip().lstrip("{").rstrip("}")
                    if(param_check != ""):
                        uri_params.append(get_route[i])
                    param_read_flag = True
                    i += 1
                    ri += 1

                elif(array_key_exists(ri, user_route) and array_key_exists(i, get_route) and get_route[i] == user_route[ri] and not param_read_flag or mode and not param_read_flag):
                    i += 1
                    ri += 1

                elif(param_read_flag and array_key_exists(i, get_route) or mode and not param_read_flag):
                    uri_params.append(get_route[i])
                    if(param_read_count is not None and param_read_max is not None):
                        if(param_read_max == param_read_count):
                            param_read_flag = False
                            break
                    i += 1
                    ri += 1
                    param_read_count += 1

                elif(param_read_flag and array_key_exists(i, get_route) or mode and param_read_flag):
                    param_read_flag = False
                    break
                else:
                    return False
            else:
                break
        return uri_params

    @staticmethod
    def RoutingEntrance(user_route: str, get_route: str):
        Me = GateWay()
        parsed_url = Me.RoutingCore(user_route, get_route)
        if(type(parsed_url) == list):
            #ここにセッションにインサートする処理を記述する
            pass

    @staticmethod
    def RoutingJudgement(user_route: str, get_route: str):
        Me = GateWay()
        parsed_url = Me.RoutingCore(user_route, get_route)
        if (type(parsed_url) == bool):
            return False
        else:
            return True