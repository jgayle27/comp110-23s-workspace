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


    # for key in head_dict:
    #     while idx < num_rows:
    #         num_list: list[str] = []
    #         num_list.append(head_dict[key])
    #         idx += 1
    # while idx_list <= len(num_list):
    #     print(num_list)
    #     new_dict[num_list[idx_list]] = head_dict[num_list[idx_list]]
    #     idx_list += 1