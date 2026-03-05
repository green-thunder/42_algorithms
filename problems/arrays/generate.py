def generate_row(prev):
    next_ = [1]
    for i in range(len(prev) - 1):
        next_.append(prev[i] + prev[i+1])
    next_.append(1)
    return next_

def generate_42(n):
    if n == 0: return []
    row = [1]
    triangle = [row]
    for i in range(n-1):
        row = generate_row(row)
        triangle.append(row)
    return triangle


def generate_my(n):
    if n == 0: return []
    triangle = [[1]]
    for i in range(1, n):
        prev = triangle[-1]
        row = [1]
        for j in range(1, i):
            row.append(prev[j-1] + prev[j])
        row.append(1)
        triangle.append(row)
    return triangle

if __name__ == "__main__":
    try:
        from performance_tester import PerformanceTester
    except ModuleNotFoundError:
        import sys
        from pathlib import Path
        sys.path.append(str(Path(__file__).resolve().parents[2]))
        from performance_tester import PerformanceTester

    # Performance Test
    tester = PerformanceTester(trials=100)
    tester.compare_all([generate_42, generate_my], lambda: 500)
