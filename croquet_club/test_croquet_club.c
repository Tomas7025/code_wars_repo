#include <stddef.h>
#include <stdbool.h>
#include <criterion/criterion.h>

enum membership {OPEN = 1, SENIOR = 2};

extern void get_membership_type (size_t n, const int members[n][2], enum membership memberships[n]);
static void do_test (size_t n, const int members[n][2], const enum membership expected[n], enum membership user_array[n]);

#define ARR_LEN(array) (sizeof(array) / sizeof(*(array)))

#define sample_test(members, expected) do_test(ARR_LEN(members), members, expected, (enum membership[ARR_LEN(members)]){0})

Test(tests_suite, sample_tests)
{
    sample_test(((const int[][2]){
		{45, 12}, {55,21}, {19, -2}, {104, 20}
	}),((const enum membership[])
		{OPEN, SENIOR, OPEN, SENIOR}
	));
    sample_test(((const int[][2]){
		{3, 12}, {55,1}, {91, -2}, {53, 23}
	}),((const enum membership[])
		{OPEN, OPEN, OPEN, OPEN}
	));
    sample_test(((const int[][2]){
		{59, 12}, {55,-1}, {12, -2}, {12, 12}
	}),((const enum membership[])
		{SENIOR, OPEN, OPEN, OPEN}
	));
}

extern void open_or_senior (size_t n, const int members[n][2], enum membership memberships[n]);

static void do_test (size_t n, const int members[n][2], const enum membership expected[n], enum membership user_array[n])
{
	open_or_senior(n, members, user_array);

	for (size_t i = 0; i < n; i++) {
		if (expected[i] != user_array[i]) {
			cr_assert_fail("for age = %d and handicap = %d, expected %s",
				members[i][0], members[i][1], expected[i] == SENIOR ? "SENIOR" : "OPEN"
			);
		}
	}
	cr_assert(true);
}