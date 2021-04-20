#!/usr/bin/env python3

from arc_consistency_fixtures import unpack_fixture, list_all_fixtures

from arc_consistency import ac_01_pure_function, ac_03_pure_function, print_domains


def make_indented_printer(indent):
    def printer(str_to_print):
        print("  " * indent + str_to_print)

    return printer


def test_ac_algorithm(ac_algorithm_to_test, fixture):
    (case_name, domains, constraints, expected_domains) = unpack_fixture(fixture)
    actual_domains = ac_algorithm_to_test(domains, constraints)
    passed = actual_domains == expected_domains
    outcome = "PASS" if passed else "FAIL"
    print("[{}] CASE {}".format(outcome, case_name))
    if not passed:
        printer = make_indented_printer(1)
        printer("Start domains:")
        print_domains(domains, printer)
        printer("Expected result domains:")
        print_domains(expected_domains, printer)
        printer("Actual result domains:")
        print_domains(actual_domains, printer)
        return False
    return True


def run_all_tests_on_ac_algorithm(ac_algorithm_to_test):
    print("-" * 60)
    print("RUNNING TESTS ON {}".format(ac_algorithm_to_test.__name__))
    print("-" * 60)
    fixtures = list_all_fixtures()
    failed = len(fixtures)
    for fixture in fixtures:
        if test_ac_algorithm(ac_algorithm_to_test, fixture):
            failed -= 1
    if failed == 0:
        print("All tests passed")
    else:
        print("{} failed of {}".format(failed, len(fixtures)))


def run_all_tests_on_ac_01_pure_function():
    run_all_tests_on_ac_algorithm(ac_01_pure_function)


def run_all_tests_on_ac_03_pure_function():
    run_all_tests_on_ac_algorithm(ac_03_pure_function)


def main():
    run_all_tests_on_ac_01_pure_function()
    run_all_tests_on_ac_03_pure_function()


##############################################################################

if __name__ == "__main__":
    main()
