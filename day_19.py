import fileinput
import re
from functools import cache

NUMBER_RE = re.compile(r'\d+')


def main():
    blueprints: list[tuple[int, int, tuple[int, int], tuple[int, int]]] = list(map(parse_blueprint, fileinput.input()))

    print(*part_1_and_2(blueprints), sep='\n')


def parse_blueprint(raw_blueprint: str) -> tuple[int, int, tuple[int, int], tuple[int, int]]:
    costs = list(map(int, NUMBER_RE.findall(raw_blueprint)))

    return costs[1], costs[2], (costs[3], costs[4]), (costs[5], costs[6])


def part_1_and_2(blueprints: list[tuple[int, int, tuple[int, int], tuple[int, int]]]) -> tuple[int, int]:
    part_1 = 0
    part_2 = 1

    for id_, (ore_robot_ore_cost, clay_robot_ore_cost, (obsidian_robot_ore_cost, obsidian_robot_clay_cost),
              (geode_robot_ore_cost, geode_robot_obsidian_cost)) in enumerate(blueprints, 1):
        @cache
        def next_minute(time_left: int, ore_robots: int, clay_robots: int, obsidian_robots: int,
                        ore: int, clay: int, obsidian: int):
            geodes = []
            n = 4

            if ore >= geode_robot_ore_cost and obsidian >= geode_robot_obsidian_cost:
                if time_left >= 3:
                    geodes.append(time_left - 1 + next_minute(time_left - 1,
                                                              ore_robots, clay_robots, obsidian_robots,
                                                              ore + ore_robots - geode_robot_ore_cost,
                                                              clay + clay_robots,
                                                              obsidian + obsidian_robots - geode_robot_obsidian_cost))
                else:
                    geodes.append(time_left - 1)
            elif time_left >= 3:
                if obsidian_robots == 0:
                    n -= 1

                if ore >= obsidian_robot_ore_cost and clay >= obsidian_robot_clay_cost:
                    geodes.append(next_minute(time_left - 1,
                                              ore_robots, clay_robots, obsidian_robots + 1,
                                              ore + ore_robots - obsidian_robot_ore_cost,
                                              clay + clay_robots - obsidian_robot_clay_cost,
                                              obsidian + obsidian_robots))
                elif clay_robots == 0:
                    n -= 1
                if ore >= clay_robot_ore_cost:
                    geodes.append(next_minute(time_left - 1,
                                              ore_robots, clay_robots + 1, obsidian_robots,
                                              ore + ore_robots - clay_robot_ore_cost,
                                              clay + clay_robots,
                                              obsidian + obsidian_robots))
                if ore >= ore_robot_ore_cost:
                    geodes.append(next_minute(time_left - 1,
                                              ore_robots + 1, clay_robots, obsidian_robots,
                                              ore + ore_robots - ore_robot_ore_cost,
                                              clay + clay_robots,
                                              obsidian + obsidian_robots))
                if len(geodes) < n:
                    geodes.append(next_minute(time_left - 1,
                                              ore_robots, clay_robots, obsidian_robots,
                                              ore + ore_robots,
                                              clay + clay_robots,
                                              obsidian + obsidian_robots))

            return max(geodes, default=0)

        part_1 += id_ * next_minute(24, 1, 0, 0, 0, 0, 0)
        if id_ <= 3:
            part_2 *= next_minute(32, 1, 0, 0, 0, 0, 0)
        next_minute.cache_clear()

    return part_1, part_2


if __name__ == '__main__':
    main()
