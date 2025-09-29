import numpy as np

# Load high-symmetry k-points from a file
def load_highsym(filename="highsym.data"):
    kpoints = []
    labels = []
    with open(filename, 'r') as f:
        for line in f:
            if not line.strip():
                continue
            parts = line.split()
            vec = list(map(float, parts[:3]))
            label = parts[4] if len(parts) > 4 else ""
            kpoints.append(vec)
            labels.append(label)
    return np.array(kpoints), labels

# Interpolate between points
def interpolate_kpath(kpoints, n_intervals):
    interpolated = []
    label_points = []
    total = 0
    for i in range(len(kpoints) - 1):
        start = kpoints[i]
        end = kpoints[i + 1]
        for j in range(n_intervals):
            t = j / n_intervals
            vec = (1 - t) * np.array(start) + t * np.array(end)
            interpolated.append(vec.tolist())
            label_points.append("")
            total += 1
    # Add last point
    interpolated.append(kpoints[-1].tolist())
    label_points.append("")
    return interpolated, total + 1

# Write to VASP-style KPOINTS file
def write_kpoints(kpath, labels, filename="KPOINTS", style="Reciprocal"):
    with open(filename, 'w') as f:
        f.write("Explicit k-points\n")
        f.write(f"{len(kpath)}\n")
        f.write(f"{style}\n")
        for i, kp in enumerate(kpath):
            label = labels[i] if i < len(labels) else ""
            label = f" {label}" if label else ""
            f.write(f"{kp[0]:10.7f} {kp[1]:10.7f} {kp[2]:10.7f}   1.000000{label}\n")
    print(f"Saved {len(kpath)} k-points to {filename}")

# Main logic
def main():
    n_points = 10  # points *between* pairs
    kpts, labels = load_highsym("highsym.data")
    kpath, total = interpolate_kpath(kpts, n_points)
    
    # Reinsert labels at the right indices (start of each segment)
    label_indices = list(range(0, len(kpath), n_points))
    label_map = {idx: lbl for idx, lbl in zip(label_indices, labels)}
    final_labels = [label_map.get(i, "") for i in range(len(kpath))]

    write_kpoints(kpath, final_labels)

if __name__ == "__main__":
    main()


