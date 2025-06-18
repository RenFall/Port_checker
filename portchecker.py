import psutil

def get_used_ports():
    ports_info = {}
    for conn in psutil.net_connections(kind='inet'):
        if conn.laddr.port != 0 and conn.status == psutil.CONN_LISTEN:  # Фильтруем только прослушиваемые порты
            try:
                # Получаем информацию о процессе по PID
                process = psutil.Process(conn.pid) if conn.pid else None
                process_name = process.name() if process else "N/A"
                process_status = process.status() if process else "N/A"
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                process_name = "N/A"
                process_status = "N/A"

            # Добавляем информацию о порте в словарь, чтобы избежать дубликатов
            if conn.laddr.port not in ports_info:
                ports_info[conn.laddr.port] = {
                    'port': conn.laddr.port,
                    'pid': conn.pid,
                    'process_name': process_name,
                    'status': process_status
                }

    return sorted(ports_info.values(), key=lambda x: x['port'])

if __name__ == "__main__":
    used_ports = get_used_ports()
    print("Занятые порты и информация о процессах:")
    for port_info in used_ports:
        print(f"Порт: {port_info['port']}, PID: {port_info['pid']}, Процесс: {port_info['process_name']}, Статус: {port_info['status']}")
