import speedtest, sched, time, sys, csv

RESULT = [['time', 'download', 'upload', 'latency', 'server-url']]

def main():
    number_of_runs = sys_argument_handler()
    s = sched.scheduler(time.time, time.sleep)
    for i in range(number_of_runs):
        s.enter(60,1,calc_speed)

    s.run()
    print(RESULT)
    t = time.time()
    filename = str(time.strftime('%Y-%m-%d %H-%M-%S.csv', time.localtime(t)))
    print_csv(filename, RESULT)

    # print(result)
    # s = speedtest.Speedtest()
    # s.get_best_server()
    # s.download()
    # s.upload()
    #
    # results_dict = s.results.dict()
    #
    # # print(results_dict)
    # print(s.results.download)
    # print(transform_bit_to_mbit(s.results.download))
    # print(s.results.upload)
    # print(transform_bit_to_mbit(s.results.upload))
    # print(s.results.server['latency'])
    # print(s.results.timestamp)

def print_csv(name, data):
    with open(name, mode = 'w') as result_file:
        csv_writer = csv.writer(result_file, delimiter = ',')
        csv_writer.writerows(data)


def sys_argument_handler():
    if len(sys.argv) != 2:
        print('Invalid number of arguments!')
        exit()
    else:
        return int(sys.argv[1])


def calc_speed():
    global RESULT
    s = speedtest.Speedtest()
    s.get_best_server()
    s.download()
    s.upload()
    RESULT.append([s.results.timestamp,
            transform_bit_to_mbit(s.results.download),
            transform_bit_to_mbit(s.results.upload),
            s.results.server['latency'],
            s.results.server['url']])


def transform_bit_to_mbit(bits):
    return bits/1000000


if __name__ == '__main__':
    main()
