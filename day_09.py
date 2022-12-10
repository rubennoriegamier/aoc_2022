import fileinput


def main():
    motions: list[tuple[int, int]] = list(map(parse_motion, fileinput.input()))

    print(part_1(motions))
    print(part_2(motions, 10))


def parse_motion(raw_motion: str) -> tuple[int, int]:
    raw_dir, raw_count = raw_motion.split()

    match raw_dir:
        case 'U':
            return int(raw_count), 0
        case 'R':
            return 0, int(raw_count)
        case 'D':
            return -int(raw_count), 0
        case 'L':
            return 0, -int(raw_count)


def part_1(motions: list[tuple[int, int]]) -> int:
    coords = {(0, 0)}
    head_y, head_x, tail_y, tail_x = 0, 0, 0, 0

    for offset_y, offset_x in motions:
        head_y += offset_y
        head_x += offset_x

        while abs(head_y - tail_y) > 1 or abs(head_x - tail_x) > 1:
            tail_y += max(min(head_y - tail_y, 1), -1)
            tail_x += max(min(head_x - tail_x, 1), -1)
            coords.add((tail_y, tail_x))

    return len(coords)


def part_2(head_motions: list[tuple[int, int]], knots: int) -> int:
    for _ in range(knots - 2):
        tail_motions = []
        head_y, head_x, tail_y, tail_x = 0, 0, 0, 0

        for offset_y, offset_x in head_motions:
            head_y += offset_y
            head_x += offset_x

            if abs(head_y - tail_y) * abs(head_x - tail_x) > 1:
                move_y = abs(head_y - tail_y)
                move_x = abs(head_x - tail_x)
                move = min(move_y, move_x) - (move_y == move_x)
                move_y = move * (1 if tail_y < head_y else -1)
                move_x = move * (1 if tail_x < head_x else -1)
                tail_motions.append((move_y, move_x))
                tail_y += move_y
                tail_x += move_x

            if abs(head_y - tail_y) > 1 or abs(head_x - tail_x) > 1:
                move_y = max(abs(head_y - tail_y) - 1, 0) * (1 if tail_y < head_y else -1)
                move_x = max(abs(head_x - tail_x) - 1, 0) * (1 if tail_x < head_x else -1)
                tail_motions.append((move_y, move_x))
                tail_y += move_y
                tail_x += move_x

        head_motions = tail_motions

    return part_1(head_motions)


if __name__ == '__main__':
    main()
