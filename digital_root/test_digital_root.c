#include <criterion/criterion.h>

int digital_root(int);

Test(Fixed, Digital_root) {
    cr_assert_eq(digital_root(16), 7, "Expected %d, instead got %d", 7, digital_root(16));
    cr_assert_eq(digital_root(195), 6, "Expected %d, instead got %d", 6, digital_root(195));
    cr_assert_eq(digital_root(992), 2, "Expected %d, instead got %d", 2, digital_root(992));
    cr_assert_eq(digital_root(167346), 9, "Expected %d, instead got %d", 9, digital_root(167346));
    cr_assert_eq(digital_root(0), 0, "Expected %d, instead got %d", 0, digital_root(0));
}
