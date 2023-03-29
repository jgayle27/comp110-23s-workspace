    # for key in new_dict:
    #    while (idx <= len(new_dict) - 1):
    #        if (new_dict[key] > compare_list[idx]):
    #            top_color = key
    #            top_color_list.append(key)
    #            print(top_color)
    #        else:
    #            idx += 1
    #    idx = 0
    
    # for key in new_dict:
    #     key_bool: bool = False
    #     while (idx <= len(new_dict) - 1 and not key_bool):
    #         if (new_dict[key] >= compare_list[idx]):
    #             key_bool = True
    #             top_color = key
    #         if (new_dict[key] == compare_list[idx]):
    #             top_color_list.append(key)
    #             idx += 1
    #         else:
    #             idx += 1
    #     idx = 0
    #     top_color = top_color_list[0]
    # return (top_color)
    for key in new_dict:
        compare_list.append(new_dict[key])