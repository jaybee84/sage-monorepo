/* eslint-disable */
module.exports = {
  displayName: 'challenge-bot',
  preset: '../../../jest.preset.js',
  transform: {
    '^.+\\.[tj]s$': ['ts-jest', { tsconfig: '<rootDir>/tsconfig.spec.json' } ],
  },
  moduleFileExtensions: ['ts', 'js', 'html'],
  coverageDirectory: '../../../coverage/apps/openchallenges/bot',
  testMatch: ['<rootDir>/test/**/*.spec.ts'],
};