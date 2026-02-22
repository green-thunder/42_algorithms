import time
from concurrent.futures import ProcessPoolExecutor
from functools import partial
import pickle

def _run_worker(func, trials, data_source):
    durations = []
    for _ in range(trials):
        data = data_source() if callable(data_source) else list(data_source)
        start = time.perf_counter()
        func(data)
        end = time.perf_counter()
        durations.append(end - start)
    avg_time = sum(durations) / trials
    return (func.__name__, avg_time)

def _assert_picklable(obj, what: str):
    try:
        pickle.dumps(obj)
    except Exception as exc:
        raise TypeError(
            f"{what} must be pickleable for ProcessPoolExecutor. "
            "Define it at module top-level (not nested), avoid lambdas, "
            "and use functools.partial to bind arguments."
        ) from exc

class PerformanceTester:
    def __init__(self, trials=20):
        self.trials = trials

    def run(self, func, data_source):
        durations = []
        for _ in range(self.trials):
            data = data_source() if callable(data_source) else list(data_source)
            start = time.perf_counter()
            func(data)
            end = time.perf_counter()
            durations.append(end - start)
        return sum(durations) / self.trials

    def _print_results(self, results):
        """Helper to print results in the exact same format for both methods."""
        sorted_results = sorted(results.items(), key=lambda item: item[1])
        fastest_name, fastest_time = sorted_results[0]
        
        print("-" * 40)
        print(f"Winner: '{fastest_name}' is the fastest.")
        for name, time_val in sorted_results[1:]:
            diff = time_val - fastest_time
            pct = (diff / fastest_time) * 100
            print(f"  '{name}' is {pct:.1f}% slower than the winner.")

    def compare_all(self, functions, data_source):
        print(f"Benchmarking {len(functions)} methods sequentially...")
        results = {func.__name__: self.run(func, data_source) for func in functions}
        
        for name, avg_time in results.items():
            print(f"  {name:<20}: {avg_time:.6f}s")
        self._print_results(results)

    def compare_parallel(self, functions, data_source):
        print(f"Benchmarking {len(functions)} methods in parallel...")

        _assert_picklable(data_source, "data_source")
        for func in functions:
            _assert_picklable(func, f"function '{func.__name__}'")

        with ProcessPoolExecutor() as executor:
            worker_func = partial(_run_worker, trials=self.trials, data_source=data_source)
            results = dict(executor.map(worker_func, functions))
        
        for name, avg_time in results.items():
            print(f"  {name:<20}: {avg_time:.6f}s")
        self._print_results(results)
