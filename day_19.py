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
        max_ore_robots = max(clay_robot_ore_cost, obsidian_robot_ore_cost, geode_robot_ore_cost)

        @cache
        def next_minute(time_left: int, ore_robots: int, clay_robots: int, obsidian_robots: int,
                        ore: int, clay: int, obsidian: int):
            if time_left < 2:
                return 0

            geodes = []
            buildable = 4

            next_clay = (clay_robots
                         if clay_robots == obsidian_robot_clay_cost or obsidian_robots == geode_robot_obsidian_cost
                         else clay + clay_robots)
            next_obsidian = (obsidian_robots if obsidian_robots == geode_robot_obsidian_cost
                             else obsidian + obsidian_robots)

            # New geode robot
            if obsidian_robots == 0:
                buildable -= 1
            elif ore >= geode_robot_ore_cost and obsidian >= geode_robot_obsidian_cost:
                next_ore = ore_robots if ore_robots == max_ore_robots else ore + ore_robots - geode_robot_ore_cost
                next_obsidian_ = (obsidian_robots if obsidian_robots == geode_robot_obsidian_cost
                                  else obsidian + obsidian_robots - geode_robot_obsidian_cost)

                geodes.append(time_left - 1 + next_minute(time_left - 1,
                                                          ore_robots, clay_robots, obsidian_robots,
                                                          next_ore, next_clay, next_obsidian_))

            # New obsidian robot
            if clay_robots == 0 or obsidian_robots == geode_robot_obsidian_cost:
                buildable -= 1
            elif ore >= obsidian_robot_ore_cost and clay >= obsidian_robot_clay_cost:
                next_ore = ore_robots if ore_robots == max_ore_robots else ore + ore_robots - obsidian_robot_ore_cost
                next_clay_ = (clay_robots if clay_robots == obsidian_robot_clay_cost
                              else clay + clay_robots - obsidian_robot_clay_cost)

                geodes.append(next_minute(time_left - 1,
                                          ore_robots, clay_robots, obsidian_robots + 1,
                                          next_ore, next_clay_, next_obsidian))

            # New clay robot
            if clay_robots == obsidian_robot_clay_cost or obsidian_robots == geode_robot_obsidian_cost:
                buildable -= 1
            elif ore >= clay_robot_ore_cost:
                next_ore = ore_robots if ore_robots == max_ore_robots else ore + ore_robots - clay_robot_ore_cost

                geodes.append(next_minute(time_left - 1,
                                          ore_robots, clay_robots + 1, obsidian_robots,
                                          next_ore, next_clay, next_obsidian))

            # New ore robot
            if ore_robots == max_ore_robots:
                buildable -= 1
            elif ore >= ore_robot_ore_cost:
                next_ore = ore_robots if ore_robots == max_ore_robots else ore + ore_robots - ore_robot_ore_cost

                geodes.append(next_minute(time_left - 1,
                                          ore_robots + 1, clay_robots, obsidian_robots,
                                          next_ore, next_clay, next_obsidian))

            # No new robot
            if len(geodes) < buildable:
                next_ore = ore_robots if ore_robots == max_ore_robots else ore + ore_robots

                geodes.append(next_minute(time_left - 1,
                                          ore_robots, clay_robots, obsidian_robots,
                                          next_ore, next_clay, next_obsidian))

            return max(geodes, default=0)

        part_1 += id_ * next_minute(24, 1, 0, 0, 0, 0, 0)
        if id_ <= 3:
            part_2 *= next_minute(32, 1, 0, 0, 0, 0, 0)

    return part_1, part_2


if __name__ == '__main__':
    main()
