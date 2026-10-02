#ifndef ARP_SCAN_TIME_UTILS_H
#define ARP_SCAN_TIME_UTILS_H

#include <stdint.h>
#include <time.h>

void timespec_diff(const struct timespec *, const struct timespec *,
                   struct timespec *);
void microseconds_to_timespec(uint64_t, struct timespec *);

#endif