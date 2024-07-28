#define CATCH_CONFIG_MAIN
#include <catch2/catch.hpp>

TEST_CASE("can_you_get_the_loop") {
    REQUIRE(main() == 0);
}
