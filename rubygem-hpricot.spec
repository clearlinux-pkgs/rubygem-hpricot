#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-hpricot
Version  : 0.8.6
Release  : 4
URL      : https://rubygems.org/downloads/hpricot-0.8.6.gem
Source0  : https://rubygems.org/downloads/hpricot-0.8.6.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: rubygem-hpricot-lib
BuildRequires : ruby
BuildRequires : rubygem-bundler
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-test-unit

%description
# Hpricot, Read Any HTML
Hpricot is a fast, flexible HTML parser written in C.  It's designed to be very
accommodating (like Tanaka Akira's HTree) and to have a very helpful library
(like some JavaScript libs -- JQuery, Prototype -- give you.)  The XPath and CSS
parser, in fact, is based on John Resig's JQuery.

%package lib
Summary: lib components for the rubygem-hpricot package.
Group: Libraries

%description lib
lib components for the rubygem-hpricot package.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n hpricot-0.8.6
gem spec %{SOURCE0} -l --ruby > rubygem-hpricot.gemspec

%build
gem build rubygem-hpricot.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
hpricot-0.8.6.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/hpricot-0.8.6
ruby -v -I.:lib:test test*/test_*.rb
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/hpricot-0.8.6.gem
/usr/lib64/ruby/gems/2.3.0/extensions/x86_64-linux/2.3.0/hpricot-0.8.6/gem.build_complete
/usr/lib64/ruby/gems/2.3.0/extensions/x86_64-linux/2.3.0/hpricot-0.8.6/gem_make.out
/usr/lib64/ruby/gems/2.3.0/extensions/x86_64-linux/2.3.0/hpricot-0.8.6/mkmf.log
/usr/lib64/ruby/gems/2.3.0/gems/hpricot-0.8.6/CHANGELOG
/usr/lib64/ruby/gems/2.3.0/gems/hpricot-0.8.6/COPYING
/usr/lib64/ruby/gems/2.3.0/gems/hpricot-0.8.6/README.md
/usr/lib64/ruby/gems/2.3.0/gems/hpricot-0.8.6/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/hpricot-0.8.6/ext/fast_xs/.RUBYARCHDIR.time
/usr/lib64/ruby/gems/2.3.0/gems/hpricot-0.8.6/ext/fast_xs/FastXsService.java
/usr/lib64/ruby/gems/2.3.0/gems/hpricot-0.8.6/ext/fast_xs/Makefile
/usr/lib64/ruby/gems/2.3.0/gems/hpricot-0.8.6/ext/fast_xs/extconf.rb
/usr/lib64/ruby/gems/2.3.0/gems/hpricot-0.8.6/ext/fast_xs/fast_xs.c
/usr/lib64/ruby/gems/2.3.0/gems/hpricot-0.8.6/ext/fast_xs/fast_xs.o
/usr/lib64/ruby/gems/2.3.0/gems/hpricot-0.8.6/ext/hpricot_scan/.RUBYARCHDIR.time
/usr/lib64/ruby/gems/2.3.0/gems/hpricot-0.8.6/ext/hpricot_scan/HpricotCss.java
/usr/lib64/ruby/gems/2.3.0/gems/hpricot-0.8.6/ext/hpricot_scan/HpricotScanService.java
/usr/lib64/ruby/gems/2.3.0/gems/hpricot-0.8.6/ext/hpricot_scan/Makefile
/usr/lib64/ruby/gems/2.3.0/gems/hpricot-0.8.6/ext/hpricot_scan/extconf.rb
/usr/lib64/ruby/gems/2.3.0/gems/hpricot-0.8.6/ext/hpricot_scan/hpricot_common.rl
/usr/lib64/ruby/gems/2.3.0/gems/hpricot-0.8.6/ext/hpricot_scan/hpricot_css.c
/usr/lib64/ruby/gems/2.3.0/gems/hpricot-0.8.6/ext/hpricot_scan/hpricot_css.java.rl
/usr/lib64/ruby/gems/2.3.0/gems/hpricot-0.8.6/ext/hpricot_scan/hpricot_css.o
/usr/lib64/ruby/gems/2.3.0/gems/hpricot-0.8.6/ext/hpricot_scan/hpricot_css.rl
/usr/lib64/ruby/gems/2.3.0/gems/hpricot-0.8.6/ext/hpricot_scan/hpricot_scan.c
/usr/lib64/ruby/gems/2.3.0/gems/hpricot-0.8.6/ext/hpricot_scan/hpricot_scan.h
/usr/lib64/ruby/gems/2.3.0/gems/hpricot-0.8.6/ext/hpricot_scan/hpricot_scan.java.rl
/usr/lib64/ruby/gems/2.3.0/gems/hpricot-0.8.6/ext/hpricot_scan/hpricot_scan.o
/usr/lib64/ruby/gems/2.3.0/gems/hpricot-0.8.6/ext/hpricot_scan/hpricot_scan.rl
/usr/lib64/ruby/gems/2.3.0/gems/hpricot-0.8.6/extras/hpricot.png
/usr/lib64/ruby/gems/2.3.0/gems/hpricot-0.8.6/lib/hpricot.rb
/usr/lib64/ruby/gems/2.3.0/gems/hpricot-0.8.6/lib/hpricot/blankslate.rb
/usr/lib64/ruby/gems/2.3.0/gems/hpricot-0.8.6/lib/hpricot/builder.rb
/usr/lib64/ruby/gems/2.3.0/gems/hpricot-0.8.6/lib/hpricot/elements.rb
/usr/lib64/ruby/gems/2.3.0/gems/hpricot-0.8.6/lib/hpricot/htmlinfo.rb
/usr/lib64/ruby/gems/2.3.0/gems/hpricot-0.8.6/lib/hpricot/inspect.rb
/usr/lib64/ruby/gems/2.3.0/gems/hpricot-0.8.6/lib/hpricot/modules.rb
/usr/lib64/ruby/gems/2.3.0/gems/hpricot-0.8.6/lib/hpricot/parse.rb
/usr/lib64/ruby/gems/2.3.0/gems/hpricot-0.8.6/lib/hpricot/tag.rb
/usr/lib64/ruby/gems/2.3.0/gems/hpricot-0.8.6/lib/hpricot/tags.rb
/usr/lib64/ruby/gems/2.3.0/gems/hpricot-0.8.6/lib/hpricot/traverse.rb
/usr/lib64/ruby/gems/2.3.0/gems/hpricot-0.8.6/lib/hpricot/xchar.rb
/usr/lib64/ruby/gems/2.3.0/gems/hpricot-0.8.6/test/files/basic.xhtml
/usr/lib64/ruby/gems/2.3.0/gems/hpricot-0.8.6/test/files/bnqt.html
/usr/lib64/ruby/gems/2.3.0/gems/hpricot-0.8.6/test/files/boingboing.html
/usr/lib64/ruby/gems/2.3.0/gems/hpricot-0.8.6/test/files/cy0.html
/usr/lib64/ruby/gems/2.3.0/gems/hpricot-0.8.6/test/files/immob.html
/usr/lib64/ruby/gems/2.3.0/gems/hpricot-0.8.6/test/files/pace_application.html
/usr/lib64/ruby/gems/2.3.0/gems/hpricot-0.8.6/test/files/tenderlove.html
/usr/lib64/ruby/gems/2.3.0/gems/hpricot-0.8.6/test/files/uswebgen.html
/usr/lib64/ruby/gems/2.3.0/gems/hpricot-0.8.6/test/files/utf8.html
/usr/lib64/ruby/gems/2.3.0/gems/hpricot-0.8.6/test/files/week9.html
/usr/lib64/ruby/gems/2.3.0/gems/hpricot-0.8.6/test/files/why.xml
/usr/lib64/ruby/gems/2.3.0/gems/hpricot-0.8.6/test/load_files.rb
/usr/lib64/ruby/gems/2.3.0/gems/hpricot-0.8.6/test/nokogiri-bench.rb
/usr/lib64/ruby/gems/2.3.0/gems/hpricot-0.8.6/test/test_alter.rb
/usr/lib64/ruby/gems/2.3.0/gems/hpricot-0.8.6/test/test_builder.rb
/usr/lib64/ruby/gems/2.3.0/gems/hpricot-0.8.6/test/test_parser.rb
/usr/lib64/ruby/gems/2.3.0/gems/hpricot-0.8.6/test/test_paths.rb
/usr/lib64/ruby/gems/2.3.0/gems/hpricot-0.8.6/test/test_preserved.rb
/usr/lib64/ruby/gems/2.3.0/gems/hpricot-0.8.6/test/test_xml.rb
/usr/lib64/ruby/gems/2.3.0/specifications/hpricot-0.8.6.gemspec

%files lib
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/extensions/x86_64-linux/2.3.0/hpricot-0.8.6/fast_xs.so
/usr/lib64/ruby/gems/2.3.0/extensions/x86_64-linux/2.3.0/hpricot-0.8.6/hpricot_scan.so
/usr/lib64/ruby/gems/2.3.0/gems/hpricot-0.8.6/ext/fast_xs/fast_xs.so
/usr/lib64/ruby/gems/2.3.0/gems/hpricot-0.8.6/ext/hpricot_scan/hpricot_scan.so
/usr/lib64/ruby/gems/2.3.0/gems/hpricot-0.8.6/lib/fast_xs.so
/usr/lib64/ruby/gems/2.3.0/gems/hpricot-0.8.6/lib/hpricot_scan.so
