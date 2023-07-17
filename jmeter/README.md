
### Using the jmeter load test:

- Update `plans/test_plan.jmx`
- Update `LOAD_TEST_GOES_DOMAIN_HERE` to the domain of the web app to load test again
- Tweak any other settings as you see fit (ex. threads/controller loops)
- Start test with this:

```bash
docker run -v `pwd`/plans:/plans -v `pwd`/plans:/results justb4/jmeter -n -t /plans/test_plan.jmx -l /results/results.jtl
```
