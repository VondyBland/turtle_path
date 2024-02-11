class TurtlePath:
    def __init__(self):
        self.rows = 0
        self.cols = 0

    def scanning(self, matrix, i, j, path, all_paths):
        self.rows = len(matrix)
        self.cols = len(matrix[0])

        path.append(matrix[i][j])

        if i == self.rows - 1 and j == self.cols - 1:
            all_paths.append(list(path))
        else:
            if j + 1 < self.cols:
                self.scanning(matrix, i, j + 1, path, all_paths)
            if i + 1 < self.rows:
                self.scanning(matrix, i + 1, j, path, all_paths)
        path.pop()

    def running(self, matrix):
        all_paths = []
        path = []
        self.scanning(matrix, 0, 0, path, all_paths)
        if all_paths:
            max_sum_path = max(all_paths, key=lambda path: sum(path))
            return max_sum_path, sum(max_sum_path)
        else:
            return [], 0
