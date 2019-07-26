const inPrettier = {
  // Handled in prettier.
  'arrow-parens': 'off',
  'object-curly-newline': 'off',
  indent: 'off',
  // Prettier keeps breaking this one, so just turn it off.
  'no-confusing-arrow': 'off',
};

module.exports = {
  env: {
    browser: true,
    es6: true,
  },
  extends: 'eslint-config-airbnb',
  plugins: ['react'],
  globals: {
    graphql: false,
  },
  rules: {
    ...inPrettier,
  },
  parserOptions: {
    sourceType: 'module',
    ecmaFeatures: {
      experimentalObjectRestSpread: true,
      jsx: false,
    },
  },
};
