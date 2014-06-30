test:
	@cd tests; PYTHONPATH=.. py.test --tb=native

upload-docs:
	$(MAKE) -C docs dirhtml
	rsync -a docs/_build/dirhtml/* flow.srv.pocoo.org:/srv/websites/pluginbase.pocoo.org/static/

.PHONY: test upload-docs
