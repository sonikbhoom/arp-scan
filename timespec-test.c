#include "time-utils.h"

int
main(void) {
   struct timespec a = { 10, 100000000 };
   struct timespec b = { 8, 900000000 };
   struct timespec diff;
   struct timespec duration;

   timespec_diff(&a, &b, &diff);
   if (diff.tv_sec != 1 || diff.tv_nsec != 200000000L)
      return 1;

   timespec_diff(&b, &a, &diff);
   if (diff.tv_sec != -2 || diff.tv_nsec != 800000000L)
      return 1;

   microseconds_to_timespec(1234567, &duration);
   if (duration.tv_sec != 1 || duration.tv_nsec != 234567000L)
      return 1;

   return 0;
}