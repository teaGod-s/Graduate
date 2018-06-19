#!/usr/bin/python
# -*-coding:utf-8 -*-

import os
import sys
import json


def file_job(file_path):
    if not os.path.exists(file_path):
        print(file_path + "文件不存在,请输入绝对路径!")
    file_name = os.path.basename(file_path)
    from_fp = open(file_path, 'r')
    new_file_path = os.path.join(os.path.dirname(file_path), "new_" + file_name[:file_name.index(".")])
    if os.path.exists(new_file_path):
        os.remove(new_file_path)
    to_fp = open(new_file_path, 'a', encoding="utf8")
    flush_json(from_fp, to_fp)
    print("全部写入成功! 请查看新文件:" + new_file_path)
    from_fp.close()
    to_fp.close()


def flush_json(from_fp, to_fp):
    count = 1
    while 1:
        line = from_fp.readline().strip()
        if not line:
            print("全部加载完成")
            break
        if not line[0] == "{":
            continue
        if line[-1] == ",":
            line = line[:-1]
        job_json = json.loads(line)
        position = job_json["position"] if job_json["position"] is not None else "其他"
        position = position.replace('\t', ' ').replace('\n', ' ').strip()
        link = job_json["link"] if job_json["link"] is not None else "其他"
        link = link.replace('\t', ' ').replace('\n', ' ').strip()
        company = job_json["company"] if job_json["company"] is not None else "其他"
        company = company.replace('\t', ' ').replace('\n', ' ').strip()
        salary = job_json["salary"] if job_json["salary"] is not None else "其他"
        salary = salary.replace('\t', ' ').replace('\n', ' ').strip()
        workplace = job_json["workplace"] if job_json["workplace"] is not None else "其他"
        workplace = workplace.replace('\t', ' ').replace('\n', ' ').strip()
        education = job_json["education"] if job_json["education"] is not None else "其他"
        education = education.replace('\t', ' ').replace('\n', ' ').strip()
        experience = job_json["experience"] if job_json["experience"] is not None else "其他"
        experience = experience.replace('\t', ' ').replace('\n', ' ').strip()
        description = job_json["description"] if job_json["description"] is not None else "其他"
        description = description.replace('\t', ' ').replace('\n', ' ').strip()

        job_str = str(position + "\t" + link + "\t" + company + "\t" + salary + "\t" +
                      workplace + "\t" + education + "\t" + experience + "\t" +
                      description + "\n")
        to_fp.write(job_str)
        print("正在写入 " + str(count))
        count += 1


if __name__ == "__main__":
    if not len(sys.argv) == 2:
        print("使用方法:\npython " + sys.argv[0] + " 文件的绝对路径")
    file_job(sys.argv[1])
