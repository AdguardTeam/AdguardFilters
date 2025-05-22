// See: https://typicode.github.io/husky/how-to.html#ci-server-and-docker

// Do not initialize Husky in CI environments. GitHub Actions set the CI env variable automatically.
// See: https://docs.github.com/en/actions/learn-github-actions/variables#default-environment-variables
if (process.env.CI === 'true') {
    process.exit(0);
}

// Initialize Husky programmatically.
const husky = (await import('husky')).default;
console.log(husky());
