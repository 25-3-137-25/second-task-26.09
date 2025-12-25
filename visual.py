def plot_graph(x, y, func_name):
    print(f"\n📊 ГРАФИК {func_name}")
    print("-" * 50)
    for xi, yi in zip(x[:12], y[:12]):
        bar = "█" * int(abs(yi * 10) + 1) if abs(yi) > 0.1 else "·"
        print(f"{xi:6.2f}: {bar} ({yi:.3f})")
    print("-" * 50)

def print_table(x, y, precision=4):
    print("\n" + "="*40)
    print(f"{'X':>12} | {'Y':>12}")
    print("="*40)
    for xi, yi in zip(x, y):
        print(f"{xi:12.{precision}f} | {yi:12.{precision}f}")
    print("="*40)
