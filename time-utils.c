#include "time-utils.h"

void
timespec_diff(const struct timespec *a, const struct timespec *b,
              struct timespec *diff) {
   diff->tv_sec = a->tv_sec - b->tv_sec;
   diff->tv_nsec = a->tv_nsec - b->tv_nsec;
   if (diff->tv_nsec < 0) {
      diff->tv_sec--;
      diff->tv_nsec += 1000000000L;
   }
}

void
microseconds_to_timespec(uint64_t microseconds, struct timespec *duration) {
   duration->tv_sec = microseconds / 1000000;
   duration->tv_nsec = (long)(microseconds % 1000000) * 1000L;
}