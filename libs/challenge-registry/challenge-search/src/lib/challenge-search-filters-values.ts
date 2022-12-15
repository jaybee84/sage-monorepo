import { FilterValue } from './filter-value.model';

const thisYear = new Date().getFullYear();

const updateYear = (
  thisYear: number,
  startYearDiff: number,
  endYearDiff: number
) => {
  return {
    start: `${thisYear + startYearDiff}-01-01`,
    end: `${thisYear + endYearDiff}-12-31`,
  };
};

export const challengeStartYearRangeFilterValues: FilterValue[] = [
  {
    value: updateYear(thisYear, -30, 10),
    label: 'All',
    active: true,
  },
  {
    value: updateYear(thisYear, 1, 1),
    label: (thisYear + 1).toString(),
    active: false,
  },
  {
    value: updateYear(thisYear, 0, 0),
    label: thisYear.toString(),
    active: false,
  },
  {
    value: updateYear(thisYear, -1, -1),
    label: (thisYear - 1).toString(),
    active: false,
  },
  {
    value: updateYear(thisYear, -6, -2),
    label: thisYear - 6 + ' - ' + (thisYear - 2),
    active: false,
  },
  {
    value: updateYear(thisYear, -11, -7),
    label: thisYear - 11 + ' - ' + (thisYear - 7),
    active: false,
  },
  {
    value: updateYear(thisYear, -21, -12),
    label: thisYear - 21 + ' - ' + (thisYear - 12),
    active: false,
  },
  {
    value: 'custom',
    label: 'Custom',
    active: false,
  },
];
