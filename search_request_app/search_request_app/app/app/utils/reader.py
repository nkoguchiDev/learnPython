path = "./container/nginx/01/log/access.log"


class Reader:
    def __init__(self, path):
        self._path = path

    def read(self):
        with open(self._path) as f:
            self._line = [
                line.replace(
                    '"',
                    "").replace(
                    "\n",
                    "").replace(
                    "[",
                    "").replace(
                    "]",
                    "") for line in f.readlines()]

    def get_line(self):
        for calam in self._line:
            calam = calam.split(" ")
            [ip, date, method, path, status_code, id] = [
                calam[0], calam[3], calam[5], calam[6], calam[8], calam[13]]
            print(
                f"""
                ip: {ip}
                date: {date}
                method: {method}
                path: {path}
                status_code: {status_code}
                id: {id}
                """)


if __name__ == '__main__':
    reader = Reader(path)
    reader.read()
    reader.get_line()
