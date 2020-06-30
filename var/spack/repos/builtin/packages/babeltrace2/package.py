# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Babeltrace2(AutotoolsPackage):
    """Babeltrace /ˈbæbəltreɪs/, an EfficiOS project, is an open-source trace manipulation toolkit."""

    homepage = "https://babeltrace.org/"
    url      = "https://www.efficios.com/files/babeltrace/babeltrace2-2.0.2.tar.bz2"

    maintainers = ['Kerilk']

    version('2.0.3',      sha256='a53625152554102d868ba8395347d0daba0bec9c4b854c3e9bd97c77b0bf04a0')
    version('2.0.2',      sha256='30c684e8b948fb79b12ee6861957dc3b99f2aba33a11cfb7fbe598e8a4aae24a')

    variant('python', default=True, description="With python bindings")

    depends_on('elfutils')
    depends_on('python', when='+python')
    depends_on('swig', when='+python')

    def configure_args(self):
        args = []
        if '+python' in self.spec:
            args.append('--enable-python-bindings')
        return args
