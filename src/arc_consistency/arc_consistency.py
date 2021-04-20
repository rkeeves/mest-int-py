#!/usr/bin/env python3

DEBUG_SHOW_REVISE_CALL_INFO = True

DEBUG_SHOW_REVISE_RESULT_INFO = True

DEBUG_SHOW_REVISE_COUNT = True


def default_printer(str_to_print):
    print(str_to_print)


def print_domains(domains, printer=default_printer):
    for var, values in domains.items():
        printer("{} : {}".format(var, values))


def revise_pure_function(constraint, domains):
    (symbol_a, symbol_b, binary_predicate_str) = constraint
    if __name__ == "__main__" and DEBUG_SHOW_REVISE_CALL_INFO:
        print(
            "Revise by ({}, {}) -> {}".format(symbol_a, symbol_b, binary_predicate_str)
        )
    a_domain = domains[symbol_a]
    b_domain = domains[symbol_b]
    new_a_domain = []
    for a_val in a_domain:
        partial_predicate = binary_predicate_str.replace(symbol_a, str(a_val))
        if any(
            eval(partial_predicate.replace(symbol_b, str(b_val))) for b_val in b_domain
        ):
            new_a_domain.append(a_val)
    new_domains = dict(domains)
    new_domains[symbol_a] = new_a_domain
    if __name__ == "__main__" and DEBUG_SHOW_REVISE_RESULT_INFO:
        print_domains(new_domains)
    return new_domains


def augment_with_inverses(constraints):
    new_constraints = []
    for constraint in constraints:
        (symbol_a, symbol_b, binary_predicate_str) = constraint
        inverse_constraint = (symbol_b, symbol_a, binary_predicate_str)
        new_constraints.append(constraint)
        new_constraints.append(inverse_constraint)
    return new_constraints


def ac_01_pure_function(domains, constraints):
    old_domains = dict(domains)
    constraints = augment_with_inverses(constraints)
    revise_count = 0
    while True:
        new_domains = dict(old_domains)
        for constraint in constraints:
            new_domains = revise_pure_function(constraint, new_domains)
            revise_count += 1
        if new_domains == old_domains:
            break
        old_domains = new_domains
    if __name__ == "__main__" and DEBUG_SHOW_REVISE_COUNT:
        print("Revise call count {}".format(revise_count))
    return new_domains


def ac_03_pure_function(domains, constraints):
    constraints = augment_with_inverses(constraints)
    constraints_to_apply = constraints[:]
    old_domains = dict(domains)
    revise_count = 0
    while len(constraints_to_apply) != 0:
        constraint = constraints_to_apply.pop(0)
        new_domains = dict(old_domains)
        new_domains = revise_pure_function(constraint, new_domains)
        revise_count += 1
        if new_domains != old_domains:
            modified_var = constraint[0]
            if len(new_domains[modified_var]) == 0:
                return new_domains
            for new_constraint in constraints:
                if new_constraint[1] == modified_var:
                    constraints_to_apply.append(new_constraint)
        old_domains = new_domains
    if __name__ == "__main__" and DEBUG_SHOW_REVISE_COUNT:
        print("Revise call count {}".format(revise_count))
    return new_domains


def main():
    example_domains = {
        "a": [1, 2, 3, 4],
        "b": [1, 2, 3, 4],
        "c": [1, 2, 3, 4],
        "d": [1, 2, 3, 4],
    }
    example_constraints = [
        ("a", "c", "a == 2 * c"),
        ("b", "c", "b > c + 1"),
        ("a", "d", "a > d - 1"),
    ]
    print("-" * 60)
    print("AC-01")
    new_domains = ac_01_pure_function(example_domains, example_constraints)
    print("The new domains, after applying AC-01, are:")
    print_domains(new_domains)
    print("-" * 60)
    print("AC-03")
    new_domains = ac_03_pure_function(example_domains, example_constraints)
    print("The new domains, after applying AC-03, are:")
    print_domains(new_domains)


##############################################################################

if __name__ == "__main__":
    main()
