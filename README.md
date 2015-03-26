# PyExifDateChange
Change the dates stored in your photo meta-information.

When going on a trip with several cameras it is possible that someone will have a different time setting.
In order to easily combine and sort photos it is important to be able to sync the time settings of the photos.
That is the precise goal for which I wrote this small script.

E.g. usage: python date_change.py <target directory> <days> <hours> <minutes> <seconds>

Additional configuration flags provide extended functionality:
# --simulate - new dates are printed to stdout but not saved in the meta-information. Useful for testing whether you picked the right offset.
# --verbose - print new dates to stdout when modifying the meta-information.
# --subtract - subtract the offset instead of adding it